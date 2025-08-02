import sys
from pathlib import Path
import fitz
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

class DocumentComparator:
    def __init__(self,base_dir):
        self.log = CustomLogger().get_logger(__name__)
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        
    
    def delete_existing_files(self):
        '''
        Delete specified files if they exist.'''
        try:
            pass
        except Exception as e:
            self.log.error(f"Error deleting existing file: {e}")
            raise DocumentPortalException("An error occurred while comparing documents", sys)
    
    def save_uploaded_files(self, reference_file, actual_file ):
        """
        Saves uploaded files to a specific directory.
        """
        try:
            self.delete_existing_files()
            self.log.info("Existing file deleted successfully ")
            ref_path=
            act_path=""
            if not reference_file.name.endswith(".pdf") or not actual_file.name.endswith(".pdf"):
                raise ValueError("Only PDF files are allowed for reference document.")
        except Exception as e:
            self.log.error(f"Error comparing documents: {e}")
            raise DocumentPortalException("An error occurred while comparing documents", sys)
    
    def read_pdf(self,pdf_path: Path) -> str:
        """
        Reads a PDF file and extracts text from each page.
        """
        try:
            with fitz.open(pdf_path) as doc:
                
                if doc.is_encrypted:
                    raise ValueError(f"PDF file {pdf_path} is encrypted and cannot be read.")
                all_text = []
                for page_num in range(doc.page_count):
                    page = doc.load_page(page_num)
                    text = page.get_text() #type: ignore
                    if text.strip():
                        all_text.append(f"\n--- Page {page_num + 1} ---\n{text}")
                    self.log.info("PDF read successfully", file=str(pdf_path), pages=len(all_text))
                return "\n".join(all_text)
        except Exception as e:
            self.log.error(f"Error comparing documents: {e}")
            raise DocumentPortalException("An error occurred while comparing documents", sys)