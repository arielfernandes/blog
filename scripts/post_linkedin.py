import sys
import json
import requests
import frontmatter
import os

def post_to_linkedin(md_file_path):
    post = frontmatter.load(md_file_path)

    title = post.get("title", "Novo post")
    tags = post.get("tags", [])
    draft = post.get("draft", False)

    if draft:
        print(f"Post é rascunho, ignorando: {title}")
        sys.exit(0)

    slug = os.path.basename(md_file_path).replace(".md", "")
    base_url = os.environ.get("SITE_BASE_URL", "").rstrip("/")
    post_url = f"{base_url}/posts/{slug}/"

    hashtags = " ".join([f"#{tag.lower().replace(' ', '')}" for tag in tags])

    text = f"{title}\n\n"
    text += f"Publiquei um novo post no meu blog, confira!\n\n"
    text += f"{post_url}"
    if hashtags:
        text += f"\n\n{hashtags}"

    access_token = os.environ["LINKEDIN_ACCESS_TOKEN"]
    author_urn = os.environ["LINKEDIN_AUTHOR_URN"]

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    payload = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "ARTICLE",
                "media": [
                    {
                        "status": "READY",
                        "originalUrl": post_url
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code == 201:
        print(f"Post publicado no LinkedIn com sucesso: {title}")
    else:
        print(f"Erro ao publicar: {response.status_code}")
        print(response.text)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1]:
        print("Nenhum arquivo novo detectado, nada a publicar.")
        sys.exit(0)
    post_to_linkedin(sys.argv[1])
