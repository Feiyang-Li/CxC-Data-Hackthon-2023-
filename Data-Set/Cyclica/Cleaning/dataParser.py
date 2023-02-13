import pandas
import category_encoders as ce


def parseData(df: pandas.DataFrame):

    # Processing categorical data
    catDataLst = ['annotation_sequence', 'entry']

    # annotation_sequence
    ce_be = ce.BinaryEncoder(cols=['annotation_sequence'])
    annotation_binary = ce_be.fit_transform(df["annotation_sequence"])

    # entry
    ce_en = ce.BinaryEncoder(cols=['entry'])
    entry_binary = ce_en.fit_transform(df["entry"])

    # Processing binary data
    binaryDataLst = ['feat_A', 'feat_C', 'feat_D', 'feat_E', 'feat_F', 'feat_G', 'feat_H', 'feat_I', 'feat_K', 'feat_L', 'feat_M', 'feat_N', 'feat_P', 'feat_Q', 'feat_R',
                     'feat_S', 'feat_T', 'feat_V', 'feat_W', 'feat_Y', 'feat_DSSP_H', 'feat_DSSP_B', 'feat_DSSP_E', 'feat_DSSP_G', 'feat_DSSP_I', 'feat_DSSP_T', 'feat_DSSP_S']

    ram2 = df[binaryDataLst].astype('int')

    # Processing number data
    # we are hard coding these min max values because we want to keep it consistent between our normalization process for the train and test dataset
    nbrDataLst = ['feat_PHI', 'feat_PSI', 'feat_TAU', 'feat_THETA', 'feat_BBSASA', 'feat_SCSASA', 'feat_pLDDT', 'feat_DSSP_6', 'feat_DSSP_7', 'feat_DSSP_8',
                  'feat_DSSP_9', 'feat_DSSP_10', 'feat_DSSP_11', 'feat_DSSP_12', 'feat_DSSP_13', 'coord_X', 'coord_Y', 'coord_Z']

    minVals = {}
    maxVals = {}
    minVals['feat_PHI'] = -3.1415571167383507
    minVals['feat_PSI'] = -3.141564187710805
    minVals['feat_TAU'] = -3.141577913855544
    minVals['feat_THETA'] = 0.0
    minVals['feat_BBSASA'] = 0.0
    minVals['feat_SCSASA'] = -2.8421709430404014e-14
    minVals['feat_pLDDT'] = 0.0
    minVals['feat_DSSP_6'] = -2281
    minVals['feat_DSSP_7'] = -4.0
    minVals['feat_DSSP_8'] = -2281
    minVals['feat_DSSP_9'] = -4.0
    minVals['feat_DSSP_10'] = -2280
    minVals['feat_DSSP_11'] = -1.8
    minVals['feat_DSSP_12'] = -2281
    minVals['feat_DSSP_13'] = -2.9
    minVals['coord_X'] = -149.3939971923828
    minVals['coord_Y'] = -114.93099975585938
    minVals['coord_Z'] = -152.83900451660156
    maxVals['feat_PHI'] = 3.141574717512001
    maxVals['feat_PSI'] = 3.141584348681896
    maxVals['feat_TAU'] = 3.1415684740186545
    maxVals['feat_THETA'] = 3.1371759095598963
    maxVals['feat_BBSASA'] = 99.33834227406886
    maxVals['feat_SCSASA'] = 220.051950154706
    maxVals['feat_pLDDT'] = 98.98
    maxVals['feat_DSSP_6'] = 2281
    maxVals['feat_DSSP_7'] = 0.0
    maxVals['feat_DSSP_8'] = 2281
    maxVals['feat_DSSP_9'] = -0.0
    maxVals['feat_DSSP_10'] = 2281
    maxVals['feat_DSSP_11'] = 0.0
    maxVals['feat_DSSP_12'] = 2282
    maxVals['feat_DSSP_13'] = -0.0
    maxVals['coord_X'] = 162.25
    maxVals['coord_Y'] = 103.13500213623048
    maxVals['coord_Z'] = 176.05999755859375

    normalized = pandas.DataFrame()
    for i in nbrDataLst:
        normalized[i] = (df[i] - minVals[i])/(maxVals[i] - minVals[i])

    # joining tables and create output
    output = annotation_binary.join(entry_binary)
    output = output.join(ram2)
    output = output.join(normalized)
    return output
