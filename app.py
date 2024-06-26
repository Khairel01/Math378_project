from vetiver import VetiverModel
from dotenv import load_dotenv, find_dotenv
import vetiver
import pins

load_dotenv(find_dotenv())

b = pins.board_folder('/data/model', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model', version = '20240421T232429Z-cf3d4')

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app
