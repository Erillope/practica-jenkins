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

@dataclass
class Membership:
    type: str
    features: List[str] = field(default_factory=list)
    premium_features: List[str] = field(default_factory=list)
    members: int = 1

    def validate_membership(self):
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
        try:
            self.validate_membership()
        except ValueError as e:
            print("Error:", e)
            return -1

        base_cost = membership_plans[self.type]
        feature_cost = sum(additional_features[self.type].get(f, 0) for f in self.features)
        premium_cost = sum(premium_features.get(f, 0) for f in self.premium_features)

        total = base_cost + feature_cost + premium_cost

        # Group Discount
        if self.members >= 2:
            print("Group discount of 10% applied.")
            total *= 0.9

        # Special Offers
        if total > 400:
            print("Special discount of $50 applied.")
            total -= 50
        elif total > 200:
            print("Special discount of $20 applied.")
            total -= 20

        # Premium surcharge
        if self.premium_features:
            print("15% surcharge for premium features applied.")
            total *= 1.15

        return round(total)

def confirm_membership(membership: Membership):
    cost = membership.calculate_cost()
    if cost == -1:
        return -1

    print("\n--- Membership Summary ---")
    print(f"Plan: {membership.type}")
    print(f"Members: {membership.members}")
    print(f"Additional Features: {', '.join(membership.features) if membership.features else 'None'}")
    print(f"Premium Features: {', '.join(membership.premium_features) if membership.premium_features else 'None'}")
    print(f"Total Cost: ${cost}")

    confirm = input("\nConfirm membership? (yes/no): ").lower()
    if confirm == 'yes':
        return cost
    else:
        print("Membership canceled.")
        return -1
