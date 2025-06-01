# 🔎 DorkScanner

**DorkScanner** is a powerful, modular Google Dork search automation tool designed for security researchers, penetration testers, and bug bounty hunters.

It scrapes Google dork entries from Exploit-DB, searches them against a target domain using Selenium, and supports advanced features like crawling discovered URLs, exporting results, retry/resume logic, and more.

---

## 🚀 Features

- ✅ Scrape dorks directly from [GHDB (Exploit-DB)](https://www.exploit-db.com/google-hacking-database)
- ✅ Search Google for each dork against a target domain
- ✅ CAPTCHA + WAF detection alert system
- ✅ Automatic screenshot capture of search results
- ✅ Crawl URLs found and extract sub-links
- ✅ CSV, Markdown, and HTML report generation
- ✅ Resume scans using `--resume` checkpoint
- ✅ Delay and rate-limit options to avoid blocking
- ✅ Progress bar and verbose mode for visibility

---

## 📦 Requirements

- Python 3.8+
- Google Chrome
- `pip install -r requirements.txt`

---

## 🧪 Usage

```bash
python3 dorkscanner.py -d target.com -f path/to/dorks.txt --html --markdown --csv --resume --crawl --delay 8
```

### Flags

| Flag         | Description                                |
|--------------|--------------------------------------------|
| `-d`         | Target domain (e.g., `example.com`)        |
| `-f`         | Path to dorks file (txt)                   |
| `--csv`      | Export results to CSV                      |
| `--html`     | Export results to HTML                     |
| `--markdown` | Export results to Markdown                 |
| `--resume`   | Resume previous scan                       |
| `--crawl`    | Crawl URLs found in search results         |
| `--delay`    | Delay (in seconds) between dorks           |
| `--headless` | Run browser in headless mode (optional)    |
| `--screenshot` | Save screenshots of results              |

---

## 🗂 Example Output

- `exports/results.csv`
- `exports/results.md`
- `exports/results.html`
- `screenshots/dork_XXXX.png`
- `crawledurls.txt`

---

## 📸 Screenshot

![sample](screenshots/sample.png)

---

## 📚 Roadmap

- [ ] Add multi-threading support
- [ ] Proxy rotation
- [ ] Burp Suite integration
- [ ] Google Custom Search API fallback
- [ ] JSON export + web viewer

---

## ⚠️ Disclaimer

This tool is for educational and authorized security research only. Do not use it against systems you don't own or have permission to test.

---

## 🤝 Contributing

PRs are welcome! Please create issues for bugs or suggestions.

---

## 📄 License

MIT License