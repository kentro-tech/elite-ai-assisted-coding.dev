from fasthtml.common import *

new_url = "https://elite-ai-assisted-coding.dev/"
def _not_found(req, exc):
    msg = Div(H1("We moved to ",A(href=new_url)(new_url))
            P("Please update your bookmark!  Redirecting in 3 seconds..."))
    return msg,Meta(http_equiv="refresh", content=f"3;url={new_url}")

app = FastHTML(exception_handlers={404:_not_found})

serve()