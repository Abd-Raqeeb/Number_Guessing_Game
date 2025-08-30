from django.shortcuts import render , redirect
import random

# Create your views here.
def GuessNumber(request):  
        if request.method == 'POST':
            user_guess = request.POST.get('user_guess')
            if not user_guess.isdigit():
                responce = {
                    'title' : 'Home Page',
                    'error' : 'Invalid input , please enter number ',
                    'msg' : 'Enjoy the Game!',
                    
                }
                return render(request , 'index.html',responce)
            user_guess = int(user_guess)
            if user_guess > 50 or user_guess < 1 :
                responce = {
                    'title' : 'Home Page',
                    'error' : 'Invalid input, Please enter a number between 1 to 50.',
                    'msg' : 'Enjoy the Game!',
                    
                }
                return render(request , 'index.html',responce)
            random_out = random.randint(1,50)
            if user_guess == random_out :
                responce={
                    'title' : 'Home Page',
                    'msg' : 'You win!🥳🥳🥳🥳🥳',
                    'user_guess' : user_guess,
                    'result' : random_out
                }
                return render(request , 'index.html',responce)
            if user_guess > random_out :
                responce = {
                    'title' : 'Home Page',
                    'msg' : 'To High',
                    'user_guess' : user_guess,
                    'result' : random_out
                }
                return render(request , 'index.html',responce)
                
            if user_guess < random_out :
                responce = {
                    'title' : 'Home Page',
                    'msg' : 'To Low',
                    'user_guess' : user_guess,
                    'result' : random_out
                }
            return render(request , 'index.html',responce)
        return render(request ,'index.html',{'title':'Home Page','msg':'Start the Game!'})

def refresh_back(request):
    return redirect('GuessNumber')