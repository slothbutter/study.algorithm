import os
import sys
import requests
import re
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter as MarkdownifyConverter

class ProgrammersParsor:
    _module_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

    def __init__(self, url):
        self.url = url
        self.html = self.request_html(self.url)
        self.soup = self.html_to_bs4()
        self.category, self.title = self.find_category_and_title()
        self.level, self.idx = self.find_level_and_idx()
        self.desc = self.find_description()
        

    def request_html(self, url):
        res = requests.get(url)
        return res.text
    
    def html_to_bs4(self):
        soup = BeautifulSoup(self.html, "lxml")
        return soup
    
    def find_category_and_title(self):
        category_title_soup = self.soup.find("ol", "breadcrumb")
        _, category_soup, tilte_soup = category_title_soup.find_all("li")
        category = category_soup.get_text()
        title = tilte_soup.get_text()
        return category, title
    
    def find_level_and_idx(self):
        metadata = self.soup.find("div", "challengeable-banner-wrapper")
        data_hackle_view = metadata["data-hackle-view"]
        level = data_hackle_view.split('"challenge_level":')[1].split(",")[0]
        idx = data_hackle_view.split('"lesson_id":')[1].split(",")[0]
        return f"Lv. {level}", idx
    
    def find_description(self):
        desc = self.soup.find("div", "guide-section-description")

        for h6 in desc.find_all("h6"):
            h6.name = "h2"
        
        for h5 in desc.find_all("h5"):
            h5.name = "h3"
        
        return MarkdownifyConverter().convert_soup(desc)
    
    def make_dir(self):
        dir_path = os.path.join(ProgrammersParsor._module_path, f"programmers/{self.level}/{self.idx}_{self.title}")
        os.makedirs(dir_path, exist_ok=True)
        return dir_path

    def write_markdown(self):
        dir_path = self.make_dir()

        readme = f"""
# [✔️/❌][{self.level}] [{self.idx}. {self.title}]({self.url})
{self.desc}
<details>
  <summary><h2>내 풀이(언어)</h2></summary>
  
  ### 정답 코드

  ```
  (작성한 정답 코드를 게시 -> 실패하면 작성x)
  ```

  ### 1차 시도

  ```
  (코드)
  ```

  (작성한 코드의 시도 과정)

  ---

  (결과)

  ### 풀이에 대한 고찰

  (정답코드의 정답 이유)

  > [!NOTE]
  > **제목**(관련 링크)<br>
  > <br>
  >관련 지식에 대한 간단 정리

  ## 다른 사람 풀이


  ### 코드
  ```
  (내용)
  ```
  ### 설명
  (내용)

  ### 출처
  (내용)

  ## 회고
  (내용)
</details>
<br>
<span style="color:gray"> #{self.category} </span>
"""
        with open(os.path.join(dir_path, "README.md"), "w") as f:
            f.write(readme)

# class BaejoonParsor:

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        if re.search("programmers", url):
            parsor = ProgrammersParsor(url=url)
    else:
        exit()
    
    parsor.write_markdown()