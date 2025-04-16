from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the network structure
model = BayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])

# Define CPDs
cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=2,
    values=[[0.3], [0.7]],
    state_names={'Disease': ['Flu', 'Cold']}
)

cpd_fever = TabularCPD(
    variable='Fever',
    variable_card=2,
    values=[
        [0.1, 0.5],  # Fever = No
        [0.9, 0.5]   # Fever = Yes
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Fever': ['No', 'Yes'],
        'Disease': ['Flu', 'Cold']
    }
)

cpd_cough = TabularCPD(
    variable='Cough',
    variable_card=2,
    values=[
        [0.2, 0.4],  # Cough = No
        [0.8, 0.6]   # Cough = Yes
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Cough': ['No', 'Yes'],
        'Disease': ['Flu', 'Cold']
    }
)

cpd_fatigue = TabularCPD(
    variable='Fatigue',
    variable_card=2,
    values=[
        [0.3, 0.7],  # Fatigue = No
        [0.7, 0.3]   # Fatigue = Yes
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Fatigue': ['No', 'Yes'],
        'Disease': ['Flu', 'Cold']
    }
)

cpd_chills = TabularCPD(
    variable='Chills',
    variable_card=2,
    values=[
        [0.4, 0.6],  # Chills = No
        [0.6, 0.4]   # Chills = Yes
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Chills': ['No', 'Yes'],
        'Disease': ['Flu', 'Cold']
    }
)

# Add CPDs to the model
model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)

# Verify the model
assert model.check_model()

# Perform inference
inference = VariableElimination(model)

# Inference Task 1: P(Disease | Fever=Yes, Cough=Yes)
result1 = inference.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes'})
print("\nProbability of disease given fever and cough:")
print(result1)

# Inference Task 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)
result2 = inference.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes', 'Chills': 'Yes'})
print("\nProbability of disease given fever, cough, and chills:")
print(result2)

# Inference Task 3: P(Fatigue=Yes | Disease=Flu)
# This is directly from the CPD, but we can verify
result3 = inference.query(variables=['Fatigue'], evidence={'Disease': 'Flu'})
print("\nProbability of fatigue given flu:")
print(result3)
