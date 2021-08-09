# PyYouTube 

Get Video Data from YouTube link 

## Installation 
```bash
pip install PyYouTube
```

## How to use it ?
### Get Videos Data 

```python
from pyyoutube import Data
yt = Data("https://youtu.be/HhHzCfrqsoE")
print(yt.data)
```

### Search Videos
```python 
from pyyoutube import Search
yt = Search("ln technical")
print(yt.videos)
```

## License 
Copyright (c) 2021 Lntechnical

This repository is licensed under the MIT license.
