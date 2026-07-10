from util import filter_mail

n = int(input())
emails = []

for _ in range(n):
    emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)