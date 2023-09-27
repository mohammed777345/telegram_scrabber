'''This module contains references to all of the different trade groups, sends signal info to them and recieves trade info'''
import json
import database_logging
import hirn
from trade import Trade
import database_logging as db

hirn_controller = hirn.HirnSignal()

async def get_trades(signal):
    '''Sends signal to the specified group'''
    if signal.origin.id == '1548802426':
        db.gen_log('Always Win Signal')
        print('Always Win Message')

    elif signal.origin.id == '1248393106':
        signal = hirn_controller.new_hirn_signal(signal)
        if signal:
            print('posting hirn signal', signal[0])
            print(signal[0].__str__())
            data = signal[0].get_dict()
            database_logging.post_signal(data)
            return signal

async def new_signal(signal, trade_stream):
    '''Controller for signals coming from a signal group'''
    # Get trade details from signal
    trades = await get_trades(signal)
    # Build and Initiate trades
    # Add trade to trade_stream
    add_trades = []
    for t in trades or []:
        new_trade = Trade(t)
        add_trades.append(new_trade)
        #print(vars(new_trade))
    await trade_stream.add_trade_to_stream(add_trades)
