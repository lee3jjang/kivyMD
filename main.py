import os
import sys
from pathlib import Path

from kivy.core.window import Window

# os.environ 설정
os.environ['KIVY_PROFILE_LANG'] = '1'
sys.path.append(os.path.abspath(__file__).split('demos')[0])
os.environ['KITCHEN_SINK_ROOT'] = str(Path(__file__).parent)
os.environ['KITCHEN_SINK_ASSETS'] = os.path.join(
    os.environ['KITCHEN_SINK_ROOT'], f'assets{os.sep}'
)

Window.softinput_mode = 'below_target' # 뭔지 모르겠음

print("---end---")