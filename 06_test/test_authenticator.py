import pytest
from authenticator import Authenticator

@pytest.fixture
def authenticator():
    authenticator = Authenticator()
    yield authenticator
    authenticator.reset()

# register() メソッドで、ユーザーが正しく登録されるか
# ユーザーを登録し、正しく登録されているかを assert で評価します。
def test_register(authenticator):
    username = 'username'
    password = 'password'
    authenticator.register(username, password)
    assert len(authenticator.users) == 1
    assert authenticator.users[username] == password

# register() メソッドで、すでに存在するユーザー名で登録を試みた場合に、エラーメッセージが出力されるか
# 同じユーザーを登録し、例外が発生することを pytest.raises() で確認します。
def test_register_duplicated(authenticator):
    username = 'username'
    password = 'password'
    authenticator.register(username, password)
    with pytest.raises(ValueError, match='エラー: ユーザーは既に存在します。'):
        authenticator.register(username, password)

# login() メソッドで、正しいユーザー名とパスワードでログインできるか
# ユーザーを登録し、ログインメッセージを assert で評価します。
def test_login(authenticator):
    username = 'username'
    password = 'password'
    authenticator.register(username, password)
    login = authenticator.login(username, password)
    assert login == 'ログイン成功'

# login() メソッドで、誤ったパスワードでエラーが出るか
# ユーザーを登録し、誤ったパスワードでログインして例外が発生することを pytest.raises() で確認します。
def test_login_error(authenticator):
    username = 'username'
    password = 'password'
    authenticator.register(username, password)
    with pytest.raises(ValueError, match='エラー: ユーザー名またはパスワードが正しくありません。'):
        authenticator.login(username, 'PASSWORD')
