# payments/views.py
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
import razorpay
import json

# Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


def donate_page(request):
    """
    Show donation page (donate.html) with Razorpay integration.
    """
    amount = 100  # in paise -> Rs. 1
    currency = 'INR'
    
    # Create order in Razorpay
    razorpay_order = razorpay_client.order.create(dict(
        amount=amount,
        currency=currency,
        payment_capture='1'  # auto capture
    ))

    context = {
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'amount': amount,
        'currency': currency,
    }
    return render(request, 'feed/donate.html', context)


@csrf_exempt
def payment_success(request):
    """
    Handle payment success (Razorpay sends back payment_id, order_id, signature).
    """
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        razorpay_order_id = data.get('razorpay_order_id')
        razorpay_payment_id = data.get('razorpay_payment_id')
        razorpay_signature = data.get('razorpay_signature')

        # Verify signature
        try:
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }
            razorpay_client.utility.verify_payment_signature(params_dict)
            return JsonResponse({"status": "Payment successful"})
        except:
            return JsonResponse({"status": "Signature verification failed"}, status=400)

    return HttpResponseBadRequest("Invalid request")
