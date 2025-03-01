<br>
<a href="https://www.numa_ultralytics.com/" target="_blank"><img src="https://raw.githubusercontent.com/numa_ultralytics/assets/main/logo/numa_ultralytics_Logotype_Original.svg" width="320" alt="numa_ultralytics logo"></a>

# 📚 numa_ultralytics Docs

[numa_ultralytics](https://www.numa_ultralytics.com/) Docs are the gateway to understanding and utilizing our cutting-edge machine learning tools. These documents are deployed to [https://docs.numa_ultralytics.com](https://docs.numa_ultralytics.com/) for your convenience.

[![pages-build-deployment](https://github.com/numa_ultralytics/docs/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/numa_ultralytics/docs/actions/workflows/pages/pages-build-deployment)
[![Check Broken links](https://github.com/numa_ultralytics/docs/actions/workflows/links.yml/badge.svg)](https://github.com/numa_ultralytics/docs/actions/workflows/links.yml)
[![Check Domains](https://github.com/numa_ultralytics/docs/actions/workflows/check_domains.yml/badge.svg)](https://github.com/numa_ultralytics/docs/actions/workflows/check_domains.yml)
[![numa_ultralytics Actions](https://github.com/numa_ultralytics/docs/actions/workflows/format.yml/badge.svg)](https://github.com/numa_ultralytics/docs/actions/workflows/format.yml)

<a href="https://discord.com/invite/numa_ultralytics"><img alt="Discord" src="https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue"></a> <a href="https://community.numa_ultralytics.com/"><img alt="numa_ultralytics Forums" src="https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.numa_ultralytics.com&logo=discourse&label=Forums&color=blue"></a> <a href="https://reddit.com/r/numa_ultralytics"><img alt="numa_ultralytics Reddit" src="https://img.shields.io/reddit/subreddit-subscribers/numa_ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue"></a>

## 🛠️ Installation

[![PyPI - Version](https://img.shields.io/pypi/v/numa_ultralytics?logo=pypi&logoColor=white)](https://pypi.org/project/numa_ultralytics/)
[![Downloads](https://static.pepy.tech/badge/numa_ultralytics)](https://www.pepy.tech/projects/numa_ultralytics)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/numa_ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/numa_ultralytics/)

To install the numa_ultralytics package in developer mode, ensure you have Git and Python 3 installed on your system. Then, follow these steps:

1. Clone the numa_ultralytics repository to your local machine using Git:

   ```bash
   git clone https://github.com/numa_ultralytics/numa_ultralytics.git
   ```

2. Navigate to the cloned repository's root directory:

   ```bash
   cd numa_ultralytics
   ```

3. Install the package in developer mode using pip (or pip3 for Python 3):

   ```bash
   pip install -e '.[dev]'
   ```

- This command installs the numa_ultralytics package along with all development dependencies, allowing you to modify the package code and have the changes immediately reflected in your Python environment.

## 🚀 Building and Serving Locally

The `mkdocs serve` command builds and serves a local version of your MkDocs documentation, ideal for development and testing:

```bash
mkdocs serve
```

- #### Command Breakdown:

  - `mkdocs` is the main MkDocs command-line interface.
  - `serve` is the subcommand to build and locally serve your documentation.

- 🧐 Note:

  - Grasp changes to the docs in real-time as `mkdocs serve` supports live reloading.
  - To stop the local server, press `CTRL+C`.

## 🌍 Building and Serving Multi-Language

Supporting multi-language documentation? Follow these steps:

1. Stage all new language \*.md files with Git:

   ```bash
   git add docs/**/*.md -f
   ```

2. Build all languages to the `/site` folder, ensuring relevant root-level files are present:

   ```bash
   # Clear existing /site directory
   rm -rf site

   # Loop through each language config file and build
   mkdocs build -f docs/mkdocs.yml
   for file in docs/mkdocs_*.yml; do
     echo "Building MkDocs site with $file"
     mkdocs build -f "$file"
   done
   ```

3. To preview your site, initiate a simple HTTP server:

   ```bash
   cd site
   python -m http.server
   # Open in your preferred browser
   ```

- 🖥️ Access the live site at `http://localhost:8000`.

## 📤 Deploying Your Documentation Site

Choose a hosting provider and deployment method for your MkDocs documentation:

- Configure `mkdocs.yml` with deployment settings.
- Use `mkdocs deploy` to build and deploy your site.

* ### GitHub Pages Deployment Example:

  ```bash
  mkdocs gh-deploy
  ```

- Update the "Custom domain" in your repository's settings for a personalized URL.

![MkDocs deployment example](https://github.com/numa_ultralytics/docs/releases/download/0/mkdocs-deployment-example.avif)

- For detailed deployment guidance, consult the [MkDocs documentation](https://www.mkdocs.org/user-guide/deploying-your-docs/).

## 💡 Contribute

We cherish the community's input as it drives numa_ultralytics open-source initiatives. Dive into the [Contributing Guide](https://docs.numa_ultralytics.com/help/contributing/) and share your thoughts via our [Survey](https://www.numa_ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A heartfelt thank you 🙏 to each contributor!

![numa_ultralytics open-source contributors](https://github.com/numa_ultralytics/docs/releases/download/0/numa_ultralytics-open-source-contributors.avif)

## 📜 License

numa_ultralytics Docs presents two licensing options:

- **AGPL-3.0 License**: Perfect for academia and open collaboration. Details are in the [LICENSE](https://github.com/numa_ultralytics/docs/blob/main/LICENSE) file.
- **Enterprise License**: Tailored for commercial usage, offering a seamless blend of numa_ultralytics technology in your products. Learn more at [numa_ultralytics Licensing](https://www.numa_ultralytics.com/license).

## ✉️ Contact

For numa_ultralytics bug reports and feature requests please visit [GitHub Issues](https://github.com/numa_ultralytics/numa_ultralytics/issues). Become a member of the numa_ultralytics [Discord](https://discord.com/invite/numa_ultralytics), [Reddit](https://www.reddit.com/r/numa_ultralytics/), or [Forums](https://community.numa_ultralytics.com/) for asking questions, sharing projects, learning discussions, or for help with all things numa_ultralytics!

<br>
<div align="center">
  <a href="https://github.com/numa_ultralytics"><img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="numa_ultralytics GitHub"></a>
  <img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/numa_ultralytics/"><img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="numa_ultralytics LinkedIn"></a>
  <img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/numa_ultralytics"><img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="numa_ultralytics Twitter"></a>
  <img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/numa_ultralytics?sub_confirmation=1"><img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="numa_ultralytics YouTube"></a>
  <img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@numa_ultralytics"><img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="numa_ultralytics TikTok"></a>
  <img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://numa_ultralytics.com/bilibili"><img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="numa_ultralytics BiliBili"></a>
  <img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/numa_ultralytics"><img src="https://github.com/numa_ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="numa_ultralytics Discord"></a>
</div>
