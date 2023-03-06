import os
import stripe
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

stripe.api_key = os.getenv("STRIPE_API_KEY")



@app.get("/payment")
async def payment_page(request:Request):
    context = {"request":request}
    return templates.TemplateResponse("payment.html", context)


@app.post("/payment")
async def make_payment(request: Request):
    # Retrieve payment details from request
    payment_details = await request.json()

    # Create a payment intent using the Stripe API
    intent = stripe.PaymentIntent.create(
        amount=payment_details["amount"],
        currency=payment_details["currency"],
        payment_method_types=["card"]
    )

    # Return a JSON response containing the payment intent ID
    return JSONResponse({"client_secret": intent.client_secret})