from setuptools import setup
name="agrinex_sim_bridge"
setup(name=name,version="0.1.0",packages=[name],data_files=[("share/ament_index/resource_index/packages",["resource/"+name]),("share/"+name,["package.xml"]),("share/"+name+"/launch",["launch/sim_state.launch.py"])],install_requires=["setuptools"],zip_safe=True,maintainer="AgriNex Maintainers",maintainer_email="maintainers@agrinex.dev",description="AgriNex simulated farm state publisher",license="Apache-2.0",entry_points={"console_scripts":["farm_state_publisher = agrinex_sim_bridge.farm_state_publisher:main"]})
