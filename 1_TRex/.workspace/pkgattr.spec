<?xml version="1.0" encoding="utf-8"?>
<ATTRIBUTES format-rev="1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<ATTRIBUTE-DEFINITIONS>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Estimated Duration [min]</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Execution Priority</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">1</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">2</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">3</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">4</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">5</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Testlevel</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<IS-MULTI-CHOICE xsi:type="boolean">True</IS-MULTI-CHOICE>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">component</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">module</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">not specified</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">subsystem</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">system</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Designer</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Type</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Design Contact</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Design Department</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Test Comment</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Tools</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">VersionCounter</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Categories</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<IS-MULTI-CHOICE xsi:type="boolean">True</IS-MULTI-CHOICE>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Administration</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">API</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Authentication</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Board</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Core</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Dashboards</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Database</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Exporting</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Externalization</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Graphical User Interface</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Interface</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Licensing</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Notifications</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Objects</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Persistence</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Project Administration</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Project Configuration</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Querying</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Reporting</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Searching</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Security</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">UI</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">User Management</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Wiki</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Severity</NAME>
			<REQUIRED xsi:type="boolean">True</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Basic</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Basic</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Basic</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Basic</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Blocker</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Blocker</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Critical</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Critical</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Detailed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Detailed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Detailed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Detailed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Major</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Major</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Minor</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Minor</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Must Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Must Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Must Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Nice to Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Nice to Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Nice to Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Normal</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Normal</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Should Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Should Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Should Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Smoke</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Smoke</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Smoke</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Smoke</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Transition</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Transition</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Transition</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Transition</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Trivial</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Trivial</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Will not Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Will not Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Will not Have</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Status</NAME>
			<REQUIRED xsi:type="boolean">True</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Accepted</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Actions Pending</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Actions Taken</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Active</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Active</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Active</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Active</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Analyzed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Approved</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Approved</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Approved</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Change Implementation</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Code Freezed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Completed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Done</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Draft</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Draft</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Draft</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Draft</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Draft</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Draft</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Draft</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Draft</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Draft</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Draft</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Feature Freezed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Implemented</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">In Progress</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">In Progress</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">In Progress</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Inactive</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Inactive</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Inactive</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Inactive</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Open</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Published</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Rejected</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Rejected</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Rejected</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Rejected</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Rejected</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Rejected</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Rejected</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Reopened</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Reviewed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Reviewed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Reviewed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Reviewed</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Verified</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Verified</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Verified</VALUE>
					</VALUE-LIST>
				</ELEMENT>
				<ELEMENT format-rev="1" xsi:type="anTreeNodeDef">
					<VALUE-LIST>
						<VALUE xsi:type="string">Verified</VALUE>
					</VALUE-LIST>
				</ELEMENT>
			</NODE-LIST>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Initial Estimate</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
		</DEFINITION>
		<DEFINITION format-rev="1" xsi:type="anAttributeDef">
			<NAME xsi:type="string">Author</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<READONLY xsi:type="boolean">True</READONLY>
		</DEFINITION>
		<DEFINITION format-rev="2" xsi:type="anAttributeTreeValueDef">
			<NAME xsi:type="string">Assignee(s)</NAME>
			<REQUIRED xsi:type="boolean">False</REQUIRED>
			<DEFAULT-VALUE xsi:type="string"/>
			<ORIGIN xsi:type="string">TMS</ORIGIN>
			<READONLY xsi:type="boolean">True</READONLY>
			<IS-MULTI-CHOICE xsi:type="boolean">True</IS-MULTI-CHOICE>
			<NODE-META-LIST-NON-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-NON-LEAFS>
			<NODE-META-LIST-LEAFS>
				<ELEMENT format-rev="1" xsi:type="anAttributeTreeNodeMetaEntryDef">
					<USE-AS-IDENTIFIER xsi:type="boolean">True</USE-AS-IDENTIFIER>
				</ELEMENT>
			</NODE-META-LIST-LEAFS>
			<NODE-LIST/>
		</DEFINITION>
	</ATTRIBUTE-DEFINITIONS>
</ATTRIBUTES>
