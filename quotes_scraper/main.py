from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os


def run_spiders() -> None:
    # Run the 'quotes' spider and execute 'load_data.py' script after completion
    process = CrawlerProcess(get_project_settings())
    process.crawl("quotes")
    process.start()

    os.system("python load_data.py")


if __name__ == "__main__":
    run_spiders()
