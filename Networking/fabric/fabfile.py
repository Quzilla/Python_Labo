from fabric import task

@task
def iso(ctx):
    from datetime import date
    print(date.today().isoformat())
