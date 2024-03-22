import pandas as pd

df = pd.read_csv('dataset.csv')

df['Timestamps'] = pd.to_datetime(df['Timestamps'])

motion_df = df[df['Motion'] == 1]
fire_df = df[df['Fire State'] == 1]
tilt_df = df[df['Tilt State'] == 1]

motion_df.to_csv('motion_detection_1.csv', index=False)
fire_df.to_csv('fire_detection_1.csv', index=False)
tilt_df.to_csv('tilt_state_1.csv', index=False)
