# workorders/storage.py
import os
from cloudinary_storage.storage import MediaCloudinaryStorage
import cloudinary.uploader

class CustomCloudinaryStorage(MediaCloudinaryStorage):
    """Custom storage that handles all file types correctly"""
    
    def _save(self, name, content):
        """Override _save to handle different file types"""
        # Get file extension
        ext = os.path.splitext(name)[1].lower()
        
        # Reset content position to start
        content.seek(0)
        
        # Images - use default storage
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']:
            print(f"📸 Uploading image using default storage: {name}")
            return super()._save(name, content)
        
        # Documents/other files - upload as raw
        else:
            print(f"📄 Uploading document as raw: {name}")
            try:
                # Upload directly as raw file
                result = cloudinary.uploader.upload(
                    content,
                    resource_type="raw",
                    public_id=name,
                    use_filename=True,
                    unique_filename=False
                )
                print(f"✅ Raw file uploaded successfully: {result.get('public_id')}")
                return result['public_id']
            except Exception as e:
                print(f"❌ Error uploading raw file: {e}")
                raise e

    def url(self, name):
        """Generate correct URLs for different file types"""
        if not name:
            return None
            
        try:
            # Determine file type from extension
            ext = os.path.splitext(name)[1].lower()
            
            if ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']:
                # Images use default URL generation
                return super().url(name)
            else:
                # Raw files need resource_type="raw"
                return cloudinary.CloudinaryImage(name).build_url(resource_type="raw")
        except Exception as e:
            print(f"Error building URL for {name}: {e}")
            return None