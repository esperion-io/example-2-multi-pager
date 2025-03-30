import os
import requests
from urllib.parse import urljoin

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Image URLs from Unsplash
images = {
    'hero-bg.jpg': 'https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1920&h=1080&fit=crop',
    'service1.jpg': 'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=800&h=600&fit=crop',
    'service2.jpg': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=600&fit=crop',
    'service3.jpg': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=800&h=600&fit=crop',
    'team1.jpg': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop',
    'team2.jpg': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&h=400&fit=crop',
    'team3.jpg': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop',
    'team4.jpg': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop',
    'client1.jpg': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&h=200&fit=crop',
    'client2.jpg': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&h=200&fit=crop',
    'client3.jpg': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&h=200&fit=crop',
    'project1.jpg': 'https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&h=600&fit=crop',
    'project2.jpg': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=600&fit=crop',
    'project3.jpg': 'https://images.unsplash.com/photo-1556911220-bff31c812dba?w=800&h=600&fit=crop'
}

# Download each image
for filename, url in images.items():
    print(f'Downloading {filename}...')
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join('images', filename), 'wb') as f:
            f.write(response.content)
        print(f'Successfully downloaded {filename}')
    else:
        print(f'Failed to download {filename}')

print('All images downloaded!') 