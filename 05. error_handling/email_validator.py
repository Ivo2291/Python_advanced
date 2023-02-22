class NameTooShortError(Exception):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(Exception):
    """Email must contain @"""


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""


def domain_validation(some_domain, domains):
    is_valid = False

    for current_domain in domains:
        if some_domain.endswith(current_domain):
            is_valid = True
            break

    return is_valid


valid_domains = [".com", ".bg", ".net", ".org"]
command = input()

while command != "End":
    email_to_check = command

    if "@" in email_to_check:
        username, domain = email_to_check.split("@")
    else:
        raise MustContainAtSymbolError("Email must contain @")

    if len(username) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    if not domain_validation(domain, valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    command = input()
