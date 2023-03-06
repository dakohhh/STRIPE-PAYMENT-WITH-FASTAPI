
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import Request
from ast import literal_eval


def customResponse(status:int, msg:str="" , success=True, data=None,):

    return JSONResponse(
        status_code=status,
        content={
        "status":status,
        "msg": msg,
        "success": success,
        "data": data if data != None else None
        }
    )


def redirect(url:str, status_code=302):
    return RedirectResponse(url, status_code=status_code)



def flash(url:str, category:str, message:str, status:int=302):
    response = RedirectResponse(url, status_code=status,)

    response.set_cookie("msg", [category, message], expires=2)

    return response



def parse_request_cookies(request:Request, key:str):

    flash_cookies = request.cookies.get(key)

    return literal_eval(flash_cookies) if flash_cookies != None else None

