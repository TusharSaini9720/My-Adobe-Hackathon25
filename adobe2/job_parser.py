def parse_job_file(job_file_path):
    """
    Parse job file to extract persona and task.
    
    Args:
        job_file_path (str): Path to the job file
        
    Returns:
        tuple: (persona, task)
    """
    try:
        with open(job_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        persona = ""
        task = ""
        for line in lines:
            line = line.strip()
            if line.lower().startswith("persona:"):
                persona = line.split(":", 1)[1].strip()
            elif line.lower().startswith("job-to-be-done:") or "job:" in line.lower():
                task = line.split(":", 1)[1].strip()
                
        if not persona or not task:
            raise ValueError("Both persona and job task must be specified in the job file")
            
        return persona, task
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Job file not found at: {job_file_path}")
    except Exception as e:
        raise Exception(f"Error parsing job file: {str(e)}")

# Make sure function is explicitly available for import
__all__ = ['parse_job_file']