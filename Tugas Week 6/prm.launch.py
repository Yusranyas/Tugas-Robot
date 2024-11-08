<launch>
  	<rosparam file="$(find prm_planner)/config/params.yaml" command="load"/>
  	<node name="prm_node" pkg="prm_planner" type="prm.py" output="screen"/>
</launch>