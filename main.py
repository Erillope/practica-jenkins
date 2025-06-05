"""
Gym Membership Management System.

This script allows users to select a gym membership plan, add optional and premium features,
calculate the total cost including discounts, and confirm the membership.
"""

from dataclasses import dataclass, field
import math
from typing import List

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


@dataclass
class Membership:
    """
    Represents a gym membership with selected features, type, and number of members.
    """
    type: str
    features: List[str] = field(default_factory=list)
    premium_features: List[str] = field(default_factory=list)
    members: int = 1

    def validate_membership(self):
        """
        Validates whether the selected membership type and features are valid.
        Raises ValueError if any issue is found.
        """
        if self.type not in membership_plans:
            raise ValueError("Invalid membership type.")

        available_features = additional_features.get(self.type, {})
        for feature in self.features:
            if feature not in available_features:
                raise ValueError(f"Feature '{feature}' is not available for {self.type} plan.")

        for feature in self.premium_features:
            if feature not in premium_features:
                raise ValueError(f"Premium feature '{feature}' is not available.")

    def calculate_cost(self):
        """
        Calculates the total cost of the membership based on selected features and discounts.
        Returns -1 if validation fails.
        """
        try:
            self.validate_membership()
        except ValueError as e:
            print("Error:", e)
            return -1

        base_cost = membership_plans[self.type]
        feature_cost = sum(additional_features[self.type].get(f, 0) for f in self.features)
        premium_cost = sum(premium_features.get(f, 0) for f in self.premium_features)

        total = base_cost + feature_cost + premium_cost

        if self.members >= 2:
            print("Group discount of 10% applied.")
            total *= 0.9

        if total > 400:
            print("Special discount of $50 applied.")
            total -= 50
        elif total > 200:
            print("Special discount of $20 applied.")
            total -= 20

        if self.premium_features:
            print("15% surcharge for premium features applied.")
            total *= 1.15

        return math.ceil(total)


def confirm_membership(membership: Membership):
    """
    Confirms the membership with the user after showing the summary and calculated cost.
    Returns the cost if confirmed, -1 otherwise.
    """
    cost = membership.calculate_cost()
    if cost == -1:
        return -1

    print("\n--- Membership Summary ---")
    print(f"Plan: {membership.type}")
    print(f"Members: {membership.members}")

    additional = ', '.join(membership.features) if membership.features else 'None'
    premium = ', '.join(membership.premium_features) if membership.premium_features else 'None'

    print(f"Additional Features: {additional}")
    print(f"Premium Features: {premium}")
    print(f"Total Cost: ${cost}")

    confirm = input("\nConfirm membership? (yes/no): ").lower()
    if confirm == 'yes':
        return cost

    print("Membership canceled.")
    return -1


def run():
    """
    Runs the interactive flow for creating and confirming a gym membership.
    """
    try:
        plan = input(f"Select a membership plan {list(membership_plans.keys())}: ")
        members = int(input("Number of members signing up together: "))

        features = []
        if plan in additional_features:
            available = additional_features[plan]
            print(f"Available features for {plan}: {available}")
            raw_features = input(
                "Enter desired additional features separated by commas (or leave blank): "
            )
            features = [f.strip() for f in raw_features.split(',') if f.strip()]

        print(f"Available premium features: {premium_features}")
        raw_premium = input("Enter desired premium features separated by commas (or leave blank): ")
        premium = [f.strip() for f in raw_premium.split(',') if f.strip()]

        membership=Membership(type=plan,features=features,premium_features=premium,members=members)

        return confirm_membership(membership)
    except ValueError as e:
        print("Input error:", e)
        return -1
