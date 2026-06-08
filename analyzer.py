class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.feedback = []

    def analyze(self):
        self.score = 0
        self.feedback = []

        if len(self.password) >= 8:
            self.score += 1
        else:
            self.feedback.append("❌ Password should be at least 8 characters")

        if len(self.password) >= 12:
            self.score += 1
        else:
            self.feedback.append("⚠️  12+ characters makes it much stronger")

        if any(c.isupper() for c in self.password):
            self.score += 1
        else:
            self.feedback.append("❌ Add at least one uppercase letter")

        if any(c.islower() for c in self.password):
            self.score += 1
        else:
            self.feedback.append("❌ Add at least one lowercase letter")

        if any(c.isdigit() for c in self.password):
            self.score += 1
        else:
            self.feedback.append("❌ Add at least one number")

        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in self.password):
            self.score += 1
        else:
            self.feedback.append("❌ Add at least one special character (!@#$...)")

        return self.score, self.feedback

    def get_strength_label(self):
        if self.score <= 2:
            return "🔴 WEAK"
        elif self.score <= 4:
            return "🟡 MODERATE"
        else:
            return "🟢 STRONG"