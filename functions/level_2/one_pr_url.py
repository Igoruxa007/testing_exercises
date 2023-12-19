

def is_github_pull_request_url(url: str) -> bool:
    splitted_url = url.split("/")
    return len(splitted_url) == 7 and splitted_url[2] == "github.com" and splitted_url[5] == "pull"

if __name__ == '__main__': # pragma: no cover
    print(is_github_pull_request_url('https://github.com/Igoruxa007/testing_exercises/pull/1'))