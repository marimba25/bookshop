from social_core.exceptions import AuthForbidden


def save_user_profile(backend, user, response, *args, **kwargs):
    print(backend.name)
    if backend.name == "google-oauth2":
        # print(response.keys())
        for key, val in response.items():
            print(f'{key}: {val}')
        if 'gender' in response.keys():
            if response['gender'] == 'male':
                user.shopuserprofile.gender = 'M'
            else:
                user.shopuserprofile.gender = 'W'
            print(response['gender'])

        if 'tagline' in response.keys():
            print(response['tagline'])
            user.shopuserprofile.tagline = response['tagline']

        if 'aboutMe' in response.keys():
            print(response['aboutMe'])
            user.shopuserprofile.aboutMe = response['aboutMe']

        if 'ageRange' in response.keys():
            minAge = response['ageRange']['min']
            print(response['ageRange'])
            if int(minAge) < 18:
                user.delete()
                raise AuthForbidden('social_core.backends.google.GoogleOAuth2')

        user.save()

    return



