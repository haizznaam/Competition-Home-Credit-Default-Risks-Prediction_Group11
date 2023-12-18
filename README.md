# Group-11_Project_Credit_Default_Risk

## Project Data Preparation and Visualization

### This is the notebook for the final Credit Default Risks project by Group 11, DSEB K63, NEU
### Team member
   * Tran Hai Nam
   * Vu Mai Dung
   * Nguyen Phuong Thao

 [Link to Presentation Slide](https://www.canva.com/design/DAF2K8vfZoo/YvpYnUuD-aOyaXAG1LSKXw/edit?utm_content=DAF2K8vfZoo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
 
 [Link to Project Report](https://docs.google.com/document/d/1z6GprK38Q8OhzTztWq2D7kwbY-2NWbNSWqGtPp395oE/edit?usp=sharing)
 
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
    - ModeReport


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
