# workorders/storage.py
import os
from django.conf import settings
from cloudinary_storage.storage import MediaCloudinaryStorage
import cloudinary.uploader

class CustomCloudinaryStorage(MediaCloudinaryStorage):
    """Custom Cloudinary storage that handles all file types properly"""
    
    def _save(self, name, content):
        # Get file extension to determine how to upload
        ext = os.path.splitext(name)[1].lower()
        
        # Image files - upload normally
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']:
            print(f"📸 Uploading image file: {name}")
            return super()._save(name, content)
        
        # Document/other files - upload as raw
        else:
            print(f"📄 Uploading document/raw file: {name}")
            try:
                # Reset content position
                content.seek(0)
                
                # Upload as raw file to Cloudinary
                result = cloudinary.uploader.upload(
                    content,
                    resource_type="raw",  # This is the key!
                    public_id=os.path.splitext(name)[0],  # Use filename without extension
                    use_filename=True,
                    unique_filename=True
                )
                print(f"✅ Raw file uploaded successfully: {result.get('public_id')}")
                return result['public_id']
                
            except Exception as e:
                print(f"❌ Error uploading raw file: {e}")
                raise e