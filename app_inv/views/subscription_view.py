from django.shortcuts import render,redirect
from app_inv.models.subscription_paln import SubscriptionPlan
from app_inv.models.user_subscription import UserSubscription
from app_inv.models.subscription_paln import SubscriptionPlan
from datetime import date,timedelta

def create_subscription(request):
    plans=SubscriptionPlan.objects.exclude(name='Free')

    if request.method == 'POST':
        selected_plan_name=request.POST.get('name') #collect value of name field.
        if not selected_plan_name:  
            return render(request, 'subscription_form.html',{
                          'plans':plans,
                          'error':'please select a plan'})
        plan=SubscriptionPlan.objects.get(name=selected_plan_name) #plan khuje ber korsi ja user select korlo

        subscription,created=UserSubscription.objects.update_or_create (
            user=request.user,
            defaults={'plan':plan,
                      'start_date': date.today(),
                      'end_date': date.today() + timedelta(days=plan.duration_days)}
                      
        )
       
        return render(request,'success.html')

        
    return render(request, 'subscription_form.html', {'plans': plans})
    

        


        
        





