from django.http import HttpRequest


def seo_attrs(request: HttpRequest):

    return {
        'seo_title': 'Training hub for investors',
        'seo_description': 'Brillianzhub - Financial and investment training hub',
        'og_type': 'website',
        'og_title': 'training hub for investors',
        'og_url': 'https://www.brillianzhub.com',
        'og_description': 'Brillianzhub - Financial and investment training hub',
        'og_image': 'https://www.brillianzhub.com/media/uploads/brillianzhub%40gmail.com/2024/04/02/growing.jpg',
        'og_site_name': 'brillianzhub.com'
    }
