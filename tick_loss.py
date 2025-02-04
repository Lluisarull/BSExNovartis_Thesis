import pandas as pd
import numpy as np

def tick_loss(alpha, returns, var):
    df = pd.DataFrame([returns, var], columns=['Return', 'VaR'])
    df['Indicator'] = np.where(df['Return'] < df['VaR'], 1, 0)
    
    t_loss = 0

    for i in df.index:
        t_loss += (alpha * (df['Return'][i] - df['VaR'][i]) * (1 - df['Indicator'][i]) + 
                 (1 - alpha) * (df['VaR'][i] - df['Return'][i]) * df['Indicator'][i])
    print(df)
    return t_loss