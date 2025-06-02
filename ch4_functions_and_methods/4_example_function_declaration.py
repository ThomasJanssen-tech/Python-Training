def checkPasswordStrength(password):
    
    if len(password) > 8:
        isStrong = True
    else:
        isStrong = False

    return isStrong
    

strongEnough = checkPasswordStrength("mysecretpassword")

if strongEnough:
    print("Your password is strong enough.")
else:
    print("Your password is not strong enough. Please choose a longer password.")