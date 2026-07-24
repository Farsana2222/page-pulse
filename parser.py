import requests
import time
from bs4 import BeautifulSoup


def analyze_page(url):
    try:
        # Automatically add https:// if missing
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        start = time.time()

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        end = time.time()

        response_time = round((end - start) * 1000, 2)

        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")

        if "text/html" not in content_type:
            return {
                "error": "This URL does not contain an HTML webpage."
            }

        soup = BeautifulSoup(response.text, "html.parser")

        title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else "No Title Found"
        )

        meta = soup.find("meta", attrs={"name": "description"})

        meta_description = (
            meta.get("content").strip()
            if meta and meta.get("content")
            else "Not Available"
        )

        h1_tags = soup.find_all("h1")

        images = soup.find_all("img")

        missing_alt = sum(
            1
            for img in images
            if not img.get("alt")
        )

        text = soup.get_text(separator=" ", strip=True)

        words = text.split()

        return {
            "url": url,
            "status": response.status_code,
            "response_time": f"{response_time} ms",
            "title": title,
            "meta_description": meta_description,
            "h1_count": len(h1_tags),
            "total_images": len(images),
            "missing_alt": missing_alt,
            "word_count": len(words)
        }

    except requests.exceptions.Timeout:
        return {
            "error": "Request timed out. Try another website."
        }

    except requests.exceptions.ConnectionError:
        return {
            "error": "Unable to connect to this website."
        }

    except requests.exceptions.HTTPError:
        if response.status_code == 403:
           return {
            "error": "This website blocks automated requests (HTTP 403). Please try another website."
           }

        elif response.status_code == 404:
            return {
            "error": "Website not found (404)."
            }

        else:
           return {
            "error": f"HTTP Error {response.status_code}"
           }

    except Exception as e:
        return {
            "error": str(e)
        }