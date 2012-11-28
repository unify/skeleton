# Unify application build script
# Part of Unify
# Copyright (C) 2012 Sebastian Fastner, Mainz, Germany

config.set("name", "$${name}")


session.permutateField("debug")
session.permutateField("es5")
session.setField("application", config.get("name"))
session.setField("application.version", "1")


@task("Clear build cache")
def clean():
    session.clean()


@task("Clear caches and build results")
def distclean():
    session.clean()
    removeDir("build")
    removeDir("external")
    removeDir("source/script")


@task("Build the full api viewer into api folder")
def api():
    ApiWriter(session).write("data")
    # Generates API browser into api folder
    Task.runTask("apibrowser", "build")


@task("Source version")
def source():
    unify.source(session, config)


@task("Build version")
def build():
    unify.build(session, config)


@task
def run():
    unify.serve()
