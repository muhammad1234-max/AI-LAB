from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the network structure
model = BayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

# Define CPDs
cpd_intelligence = TabularCPD(
    variable='Intelligence',
    variable_card=2,
    values=[[0.7], [0.3]],
    state_names={'Intelligence': ['High', 'Low']}
)

cpd_study = TabularCPD(
    variable='StudyHours',
    variable_card=2,
    values=[[0.6], [0.4]],
    state_names={'StudyHours': ['Sufficient', 'Insufficient']}
)

cpd_difficulty = TabularCPD(
    variable='Difficulty',
    variable_card=2,
    values=[[0.4], [0.6]],
    state_names={'Difficulty': ['Hard', 'Easy']}
)


cpd_grade = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        # High Int, Sufficient Study, Easy Difficulty -> most likely A
        [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],  # A
        [0.15, 0.2, 0.25, 0.3, 0.3, 0.4, 0.4, 0.5],  # B
        [0.05, 0.1, 0.15, 0.2, 0.3, 0.3, 0.4, 0.4]   # C
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2],
    state_names={
        'Grade': ['A', 'B', 'C'],
        'Intelligence': ['High', 'Low'],
        'StudyHours': ['Sufficient', 'Insufficient'],
        'Difficulty': ['Hard', 'Easy']
    }
)

cpd_pass = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.05, 0.2, 0.5],  # Pass = No
        [0.95, 0.8, 0.5]    # Pass = Yes
    ],
    evidence=['Grade'],
    evidence_card=[3],
    state_names={
        'Pass': ['No', 'Yes'],
        'Grade': ['A', 'B', 'C']
    }
)

# Add CPDs to the model
model.add_cpds(cpd_intelligence, cpd_study, cpd_difficulty, cpd_grade, cpd_pass)

# Verify the model
assert model.check_model()

# Perform inference
inference = VariableElimination(model)

# Query 1: Probability of passing given StudyHours = Sufficient, Difficulty = Hard
result1 = inference.query(variables=['Pass'], evidence={'StudyHours': 'Sufficient', 'Difficulty': 'Hard'})
print("\nProbability of passing given sufficient study hours and hard difficulty:")
print(result1)

# Query 2: Probability of High Intelligence given Pass = Yes
result2 = inference.query(variables=['Intelligence'], evidence={'Pass': 'Yes'})
print("\nProbability of high intelligence given pass:")
print(result2)
