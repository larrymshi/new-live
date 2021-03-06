import httplib2


class HttpUtility:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers
        if self.headers is None:
            self.headers = {}
        self.headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        self.headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        self.headers[
            "Cookie"] = 'll="108296"; bid=39emvg4Fy5U; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1490075263%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoErbS-KqLWVrkGxsKUBvvgGx6OPkrAbIrMV-lp0BKQIbwNvkW7mvI4_x40D0aYr-myfC25BGRTeF006RakGarK%26wd%3D%26eqid%3Dffb46cf60002fc900000000658cfb031%22%5D; _vwo_uuid_v2=5DD8628BA737EC9F2AF13BE5DC8DCEFF|798f0581c8fbef5f60eb92196d4962f6; __utmt=1; _pk_id.100001.8cb4=803be523dd8f0bb3.1487313761.11.1490076190.1490073088.; _pk_ses.100001.8cb4=*; __utma=30149280.891910915.1483680709.1490073077.1490075263.13; __utmb=30149280.5.10.1490075263; __utmc=30149280; __utmz=30149280.1490006078.11.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'

    def get(self, recall=False, encoding='utf-8'):
        try:
            return self.get_not_decode().decode(encoding)
        except UnicodeDecodeError as e:
            if not recall:
                return self.get(recall=True, encoding="ISO-8859-1")
            else:
                print(e)
                return ""
        except TimeoutError:
            return ""

    def get_not_decode(self):
        h = httplib2.Http()
        (req_headers, content) = h.request(self.url, method="GET", body=None, headers=self.headers)
        return content
