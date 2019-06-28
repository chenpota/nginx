from datetime import datetime
import urllib.parse

import flask


app = flask.Flask(__name__)


@app.route('/login')
def login():
    html = '''
<html>
  <body>
    <form action="/validate/login" method="post">
      <table>
        <tr>
          <td>Username: <input type="text" name="username" value="username"/></td>
        <tr>
          <td>Password: <input type="password" name="password" value="password"/></td>
        <tr>
          <td><input type="submit" value="Login"></td>
      </table>
      <input type="hidden" name="target" value="@TARGET@">
    </form>
  </body>
</html>
'''

    return flask.make_response((
        html.replace('@TARGET@', flask.request.headers.get('X-Target')),
        200,
        {
            'Content-Type': 'text/html;charset=UTF-8'
        }
    ))

@app.route('/logout')
def logout():
    rsp = flask.make_response((
        '',
        200,
        {}
    ))

    rsp.set_cookie(
      'custom_auth',
      '',
      expires=datetime(1970, 1, 1))

    return rsp


@app.route('/validation/cookies')
def validate_cookies():
    cookies = flask.request.cookies

    if 'custom_auth' in cookies:
        if cookies['custom_auth'] == 'username:password':
            return '', 200
        else:
            return '', 401
    else:
        return '', 401


@app.route('/validate/login', methods=['POST'])
def validate():
    request_body = flask.request.get_data().decode('utf-8')
    validate_info = urllib.parse.parse_qs(request_body)

    rsp = flask.make_response((
        '',
        302,
        {
            'Location': validate_info['target'][0]
        }
    ))

    rsp.set_cookie(
      'custom_auth',
      '{}:{}'.format(
                validate_info['username'][0],
                validate_info['password'][0]))

    return rsp

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081)
