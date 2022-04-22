import pandas as pd
from sklearn import preprocessing

                                    # Normalisasi Data
                # Variabel-Variabel pada Laporan Tahunan Bursa Efek Indonesia


# Dataframe for Rasio Aset terhadap Keuntungan
    # RAL, KAL, KAT, Total Keuntungan
df_tk = pd.DataFrame([[94, 7, 113.7, 207016], [97, 9.4, 262.5, 615308], [87, 16.6, 106.6, 463706],
                      [90, 13.4, 121.8, 682698], [89, 11.2, 98.2, 715716], [85, 9.6, 54.6, 599893],
                      [87, 5.5, 36.1, 434108], [84, 4.8, 26.1, 363730], [85, 8.6, 47.3, 782295]],
                     columns = ['RAL', 'KAL', 'KAT', 'TK'])

#                   #                   #                   #                   #

# Dataframe for Laba Bersih dan Total Aktiva (Independent Variabel)
    # Laba Bersih dan Total Aktiva YoY 2000-2014
df_lb_ta = pd.DataFrame([[4996, 521837], [1684, 728093], [13606, 689866],
                         [15134, 837383], [37809, 876097], [57449, 748562],
                         [103781, 1565783], [307702, 3390192], [231892, 1615787],
                         [341886, 2823306], [358041, 3556881], [299816, 3673291],
                         [218091, 4531882], [182412, 4476596], [392035, 5367495]],
                        columns = ['Laba Bersih', 'Total Aktiva'])

#                   #                   #                   #                   #

# Dataframe for Laba Bersih, Total Aktiva, ROA
    # Laba Bersih, Total Aktiva, ROA YoY 2000-2014
df_roa = pd.DataFrame([[4996, 521837, 0.96], [1684, 728093, 0.23], [13606, 689866, 1.97],
                         [15134, 837383, 1.81], [37809, 876097, 4.32], [57449, 748562, 7.67],
                         [103781, 1565783, 6.63], [307702, 3390192, 9.08], [231892, 1615787, 14.35],
                         [341886, 2823306, 12.11], [358041, 3556881, 10.07], [299816, 3673291, 8.16],
                         [218091, 4531882, 4.81], [182412, 4476596, 4.07], [392035, 5367495, 7.30]],
                        columns = ['Laba Bersih', 'Total Aktiva', 'ROA'])

#                   #                   #                   #                   #

# TATR & NPM
    # Total Asset Turnover Rasio & Net Profit Margin (NPM) 2000-2014
df_tatr_npm = pd.DataFrame([[16.97, 5.64], [12.30, 1.88], [13.53, 14.57],
                         [11.83, 15.27], [18.96, 22.76], [30.69, 25.01],
                         [19.34, 34.27], [17.75, 51.14], [36.30, 39.54],
                         [19.42, 62.36], [18.58, 54.18], [18.89, 43.22],
                         [14.55, 33.08], [19.44, 20.96], [17.16, 42.57]],
                        columns = ['TATR', 'NPM'])

# IHSG
    # IHSG by Open and Close (2007-2012)
df_ihsg_oc = pd.DataFrame([[1.171709, 1.805523], [1.836520, 2.745826], [2.731507, 1.355408], [1.437338, 2.534356],
                        [2.575413, 3.703512], [3.727517, 3.821992], [3.809140, 4.316687]],
                        columns = ['Open', 'Close'])

# IHSG YoY
    # IHSG YoY 2003-2012
df_ihsg_yoy = pd.DataFrame([[691.895], [1000.233], [1162.635],
                         [1805.523], [2745.826],
                         [1355.408], [2534.356], [3703.512],
                         [3821.992], [4316.687]],
                         columns = ['IHSG YoY'])


# Value and Volume Equity Trade
df_equity_val_vol = pd.DataFrame([[125.4, 234.0], [247.0, 411.8], [406.0, 401.9],
                         [445.71, 436.94], [1050.15, 1039.54],
                         [1064.53, 787.85], [975.14, 1467.66], [1176.24, 1330.87],
                         [1223.44, 1203.55], [1116.11, 1053.76]],
                         columns = ['Equity Value', 'Equity Volume'])


# Total Fund Raised (Based on Equity)
    # TFR YoY 2003-2012
df_tfr_yoy = pd.DataFrame([[14.06], [6.34], [9.66],
                         [16.38], [48.90],
                         [82.98], [14.91], [79.71],
                         [62.31], [29.97]],
                         columns = ['TFR YoY'])

# Beban Pengembangan Usaha / Trading Development
    # BPU YoY 2003-2012
df_bpu_yoy = pd.DataFrame([[4.223], [10.269], [27.864],
                          [32.424], [35.348],
                          [44.845], [48.738], [54.976],
                          [73.114], [79.832]],
                          columns = ['BPU YoY'])

# Pendapatan Usaha / Operating Revenues
    # PU YoY 2003-2012
df_pu_yoy = pd.DataFrame([[99.099], [166.166], [229.704],
                         [302.796], [647.943],
                         [634.003], [592.696], [714.307],
                         [749.796], [712.436]],
                         columns = ['PU YoY'])

# Beban Pengembangan Usaha dan Pendapatan Usaha
    # BPPU YoY 2003-2012
df_bppu = pd.DataFrame([
                        [4.223], [10.269], [27.864],
                        [32.424], [35.348],
                        [44.845], [48.738], [54.976],
                        [73.114], [79.832],
                        [99.099], [166.166], [229.704],
                        [302.796], [647.943],
                        [634.003], [592.696], [714.307],
                        [749.796], [712.436]],
                        columns = ['BPPU YoY'])

# IHSG on YoY 2008
    # IHSG Q1 - Q4 2008
df_Q2008 = pd.DataFrame([
                        [2.447], [2.349], [1.832], [1.355]],
                        columns = ['IHSG2008 YoY'])

# IHSG on YoY 2012
    # IHSG Q1 - Q4 2012
df_Q2012 = pd.DataFrame([
                        [4.121], [3.955], [4.262], [4.316]],
                        columns = ['IHSG2012 YoY'])

#                   #                   #                   #                   #


# Fungsi Hitung Normalisasi Data dengan X-Max
    # apply the maximum absolute scaling in Pandas
        # using the .abs() and .max() methods
def maximum_absolute_scaling(df):
    # copy the dataframe
    df_scaled = df.copy()
    # apply maximum absolute scaling
    for column in df_scaled.columns:
        df_scaled[column] = df_scaled[column]  / df_scaled[column].abs().max()
    return df_scaled

# Fungsi Apply X-Max pada dataframe
    # call the maximum_absolute_scaling function
 # Total Keuntungan
df_tk_scaled = maximum_absolute_scaling(df_tk)
 # Laba Bersih dan Total Keuntungan (Independent)
df_lb_ta_scaled = maximum_absolute_scaling(df_lb_ta)
 # ROA
df_roa_scaled = maximum_absolute_scaling(df_roa)
 # TATR & NPM
df_tn_scaled = maximum_absolute_scaling(df_tatr_npm)
 # IHSG by Open and Close
df_ihsg_open_close_scaled = maximum_absolute_scaling(df_ihsg_oc)
 # Value and Volume Equity Trade
df_equity_val_vol_scaled = maximum_absolute_scaling(df_equity_val_vol)
 # IHSG YoY 2003-2012
df_ihsg_yoy_scaled = maximum_absolute_scaling(df_ihsg_yoy)
 # Total Fund Raised (Based on Equity) 2003-2012
df_tfr_yoy_scaled = maximum_absolute_scaling(df_tfr_yoy)
 # Beban Pengembangan Usaha / Trading Development
df_bpu_yoy_scaled = maximum_absolute_scaling(df_bpu_yoy)
 # Pendapatan Usaha / Operating Revenues
df_pu_yoy_scaled = maximum_absolute_scaling(df_pu_yoy)
 # Beban Pengembangan Usaha dan Pendapatan Usaha
df_bppu_scaled = maximum_absolute_scaling(df_bppu)
# IHSG on YoY (Q1 - Q4) 2012
df_Q2008_scaled = maximum_absolute_scaling(df_Q2008)
 # IHSG on YoY (Q1 - Q4) 2012
df_Q2012_scaled = maximum_absolute_scaling(df_Q2012)

#

# Checkout Hasil Hitung Fungsi X-Max

 # Total Keuntungan
#print(df_tk_scaled)

 # Laba Bersih dan Total Keuntungan (Independent)
#print(df_lb_ta_scaled)

 # ROA
#print(df_roa_scaled)

 # TATR & NPM
#print(df_tn_scaled)

 # IHSG by Open and Close
#print(df_ihsg_open_close_scaled)

 # Value and Volume Equity Trade
#print(df_equity_val_vol_scaled)

 # IHSG YoY 2003-2012
#print(df_ihsg_yoy_scaled)
 
 # Total Fund Raised (Based on Equity) 2003-2012
#print(df_tfr_yoy_scaled)

 # Beban Pengembangan Usaha / Trading Development
#print(df_bpu_yoy_scaled)

 # Pendapatan Usaha / Operating Revenues
#print(df_pu_yoy_scaled)

 # # Beban Pengembangan Usaha dan Pendapatan Usaha
#print(df_bppu_scaled)

 # IHSG on YoY (Q1 - Q4) 2008
#print(df_Q2008_scaled)

 # IHSG on YoY (Q1 - Q4) 2012
#print(df_Q2012_scaled)