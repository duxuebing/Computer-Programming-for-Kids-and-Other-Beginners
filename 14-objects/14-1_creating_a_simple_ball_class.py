class Ball:  # This tells Python we’re making a class.

    # This is a method.
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"