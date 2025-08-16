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
                    public_id=name,  # Use the full name with path
                    use_filename=False,
                    unique_filename=False
                )
                print(f"✅ Raw file uploaded successfully: {result.get('public_id')}")
                return result['public_id']
                
            except Exception as e:
                print(f"❌ Error uploading raw file: {e}")
                raise e

    def url(self, name):
        """Override URL generation to handle raw files correctly"""
        try:
            # Determine if this is an image or raw file based on extension
            ext = os.path.splitext(name)[1].lower() if name else ''
            
            if ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']:
                # Images use default URL generation
                return super().url(name)
            else:
                # Raw files need resource_type="raw"
                return cloudinary.CloudinaryImage(name).build_url(resource_type="raw")
        except Exception as e:
            print(f"Error building URL for {name}: {e}")
            return None