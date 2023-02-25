# CxC-Data-Hackthon-2023-
For the data hackthon project in 2023

We are compete for Cyclica

We clearned data ensure we only have feat_PHI	feat_PSI	feat_TAU	feat_THETA	feat_BBSASA	feat_SCSASA	feat_pLDDT	feat_DSSP_6	feat_DSSP_7	feat_DSSP_8	feat_DSSP_9	feat_DSSP_10	feat_DSSP_11	feat_DSSP_12	feat_DSSP_13	coord_X	coord_Y	coord_Z.

We excluded feature of amino acid and replaced  it with the information about the polarity of that specific amino acid, thus we created features:

Non_Polar	Polar	Pos_Charge	Neg_Charge

Using feature above we predict if this section of the amino acid bind or not bind to the given drug

We used ExtraTreesClassifier with fine turn parameter for our prediction model which accheive 71.90% in our test sets.

And note this 71.90% is when we resampled the given data so there is equally number of positive binding and negative binding.

Also Note the data is very inbalance with ~96.5% of negative binding.

We tried ML model like:
- Logistic regression
- Support vector machine
- Decision Tree
- KN neighbour
- AdaBoostClassifier
- MLP classifier
- Voting classifier 
- Neuron network (using pytorch)

In the end we find out ExtraTreesClassifier model provided us with best result. 

Future imporvement:
 - Might investigate more on Neuron network, especially fine turing parameter might drastically improve the accuracy. 
 
 # label_result_Ligard_Forest_method.csv    is the final training prediction reseult
 
 Thanks for reading. 
 
 
