#Programa principal
# Gym Membership Management System

from dataclasses import dataclass, field
from typing import List, Dict

# Define Membership Plans and Features
membership_plans = {
    'Basic': 50,
    'Premium': 100,
    'Family': 150
}

additional_features = {
    'Basic': {'Group Classes': 20},
    'Premium': {'Group Classes': 20, 'Personal Training': 40},
    'Family': {'Group Classes': 30, 'Personal Training': 60}
}

premium_features = {'Exclusive Gym Access': 70, 'Specialized Training': 100}