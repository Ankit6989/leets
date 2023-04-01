"""
This file allows running the parent directory directly:
python3 src [ arg1 ... ]

This also allows packaging up as a zipapp.

If you do not need this functionality:
  - Remove this file.
  - Consider moving leets out of src.
"""

import leets.__main__

leets.__main__.main()
