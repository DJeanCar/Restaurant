

def get_avatar(backend, strategy, details, response, user=None,
			*args, **kwargs):

	city = response['hometown']['name'].split(',')[0]
	user.city = city
	url = None
	if backend.name == 'facebook':
		url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
	if backend.name == 'twitter':
		url = response.get('profile_image_url' , '').replace('_normal','')

	if url:
		user.avatar = url
		user.save()