from functions.level_2.one_pr_url import is_github_pull_request_url
import pytest


def test__is_github_pull_request_url__success_case():
    assert is_github_pull_request_url('https://github.com/Igoruxa007/testing_exercises/pull/1') == True

def test__is_github_pull_request_url__fail_case():
    assert is_github_pull_request_url('github.com/Igoruxa007/testing_exercises/pull/1') == False