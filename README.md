# Group-11_Project_Credit_Default_Risk

A credit risk modeling project in Data Preparation and Visualization

In the banking and financial industry, credit risk modeling is one of the most important tasks. Instead of using complex models, data scientists must utilize the basic model because of its explainability. Therefore, the preprocessing steps need to be carefully taken. You will have to explore the data and perform data preparation to improve the performance of the default Logistic Regression model with the given dataset.

### Team member
   * Tran Hai Nam
   * Vu Mai Dung
   * Nguyen Phuong Thao

#### [Link to Presentation Slide](https://drive.google.com/file/d/1Fd0XV_igjwwUWq57-9pmoh8Xbqon4fEG/view?usp=sharing)
 
#### [Link to Project Report](https://docs.google.com/document/d/1z6GprK38Q8OhzTztWq2D7kwbY-2NWbNSWqGtPp395oE/edit?usp=sharing)
 
 ### Assigned work:
 * Tran Hai Nam (group leader): 
    - EDA:<br /> 
      * 01_application_train - EDA
      * 02_previous_application - EDA
    - Feature Engineer: <br />
      * 00_train_test_validation_code_split (split dataset to different subsets and marked by feature tvt_code)
      * 01_application_train - FE
      * 02_Previous_application - FE
      * 07_POS_Cash_balance - FE
      * 100_combined_all_tables_fulfill (Merge data and label ) 
    - Model:
      * final_model (fillna and fitting model, evaluating model)
    
  
  * Vu Mai Dung:
    - EDA:<br />
      * 03_Bureau - EDA
      * 04_Bureau_balance - EDA
    - Feature Engineer: <br />
      * 03_Bureau - FE
      * 04_Bureau_balance - FE
    - Slide

  * Nguyen Phuong Thao
    - EDA: <br />
      * 05_credit_card_balance - EDA
      * 06_instalment_payment - EDA
      * 07_POS_CASH_balance - EDA
    - Feature Engineer: <br />
      * 05_credit_card_balance - FE
      * 06_instalment_payment - FE
    - Model:<br />
      * final_model (feature selection, evaluating model, final prediction)
    - Report<br />


Repository Organization
------------
    ├── README.md          <- The top-level README for developers using this project.
    ├── EDA
    │   ├── 01_application_train - EDA 
    │   ├── 02_previous_application - EDA
    │   ├── 03_bureau_EDA
    │   ├── 04_bureau_balance_EDA
    │   ├── 05_credit_card_balance - EDA
    │   ├── 06_installments_payments - EDA.
    │   ├── 07_POS_CASH_balance - EDA
    │   └── utils      <- Store Essential Functions for EDA.                
    ├── processing
    │   ├── features      <- Store tables after feature engineering used to merge
    │   ├── 00_train_test_validation_code_split (split dataset to different subsets and marked by feature tvt_code) 
    │   ├── 01_application_FE_full_fill
    │   ├── 02_previous_application - FE
    │   ├── 03_bureau - FE
    │   ├── 04_bureau_balance - FE
    │   ├── 05_credit_card_balance - FE
    │   ├── 06_installments_payments - FE.
    │   ├── 07_POS_CASH_balance - FE
    │   ├── 100_combined_all_tables_fullfill
    │   └── utils_feature_engineering      <- Store Essential Functions for Feature Engineering.                
    └── model
         ├── submission   <- Store prediction results.
         └──  final_model
